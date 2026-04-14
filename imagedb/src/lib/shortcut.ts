type ShortcutCallback = (event: KeyboardEvent) => void;

type ShortcutOptions = {
	preventDefault?: boolean;
	stopPropagation?: boolean;
	allowRepeat?: boolean;
	exact?: boolean;
};

type ParsedShortcut = {
	key: string;
	modifiers: {
		meta: boolean;
		ctrl: boolean;
		alt: boolean;
		shift: boolean;
	};
};

type Binding = {
	parsed: ParsedShortcut;
	callback: ShortcutCallback;
	options: Required<ShortcutOptions>;
};

const DEFAULT_OPTIONS: Required<ShortcutOptions> = {
	preventDefault: true,
	stopPropagation: false,
	allowRepeat: false,
	exact: true
};

const KEY_ALIASES: Record<string, string> = {
	esc: 'escape',
	return: 'enter',
	spacebar: 'space',
	' ': 'space'
};

const MODIFIER_ALIASES: Record<string, keyof ParsedShortcut['modifiers']> = {
	cmd: 'meta',
	command: 'meta',
	meta: 'meta',
	'⌘': 'meta',
	ctrl: 'ctrl',
	control: 'ctrl',
	'^': 'ctrl',
	alt: 'alt',
	option: 'alt',
	'⌥': 'alt',
	shift: 'shift',
	'⇧': 'shift'
};

function isMacLikePlatform() {
	if (typeof navigator === 'undefined') return false;
	return /Mac|iPhone|iPad|iPod/i.test(navigator.platform);
}

function normalizeKey(key: string) {
	const lowered = key.toLowerCase();
	if (lowered === ' ') return 'space';
	return KEY_ALIASES[lowered] ?? lowered;
}

function parseShortcut(shortcut: string): ParsedShortcut {
	const parsed: ParsedShortcut = {
		key: '',
		modifiers: {
			meta: false,
			ctrl: false,
			alt: false,
			shift: false
		}
	};

	const tokens = shortcut
		.split('+')
		.map((token) => token.trim())
		.filter(Boolean)
		.map((token) => token.toLowerCase());

	for (const token of tokens) {
		if (token === 'mod') {
			if (isMacLikePlatform()) parsed.modifiers.meta = true;
			else parsed.modifiers.ctrl = true;
			continue;
		}

		const modifier = MODIFIER_ALIASES[token];
		if (modifier) {
			parsed.modifiers[modifier] = true;
			continue;
		}

		parsed.key = normalizeKey(token);
	}

	if (!parsed.key) {
		throw new Error(`Shortcut "${shortcut}" must include a non-modifier key.`);
	}

	return parsed;
}

function isEditableTarget(target: EventTarget | null) {
	if (!(target instanceof HTMLElement)) return false;
	const tag = target.tagName;
	return target.isContentEditable || tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT';
}

function matchesShortcut(event: KeyboardEvent, binding: Binding) {
	const eventKey = normalizeKey(event.key);
	if (eventKey !== binding.parsed.key) return false;

	const { modifiers } = binding.parsed;

	if (binding.options.exact) {
		return (
			event.metaKey === modifiers.meta &&
			event.ctrlKey === modifiers.ctrl &&
			event.altKey === modifiers.alt &&
			event.shiftKey === modifiers.shift
		);
	}

	if (modifiers.meta && !event.metaKey) return false;
	if (modifiers.ctrl && !event.ctrlKey) return false;
	if (modifiers.alt && !event.altKey) return false;
	if (modifiers.shift && !event.shiftKey) return false;

	return true;
}

export function createShortcutMapper(target?: EventTarget | null) {
	const resolvedTarget = target ?? (typeof window !== 'undefined' ? window : null);
	const bindings: Binding[] = [];

	if (!(resolvedTarget && 'addEventListener' in resolvedTarget)) {
		return {
			register: () => () => {},
			destroy: () => {}
		};
	}

	const eventTarget = resolvedTarget as EventTarget & {
		addEventListener: (type: string, listener: EventListener) => void;
		removeEventListener: (type: string, listener: EventListener) => void;
	};

	const onKeydown = (event: KeyboardEvent) => {
		if (isEditableTarget(event.target)) return;

		for (const binding of bindings) {
			if (!binding.options.allowRepeat && event.repeat) continue;
			if (!matchesShortcut(event, binding)) continue;

			if (binding.options.preventDefault) event.preventDefault();
			if (binding.options.stopPropagation) event.stopPropagation();

			binding.callback(event);
		}
	};

	eventTarget.addEventListener('keydown', onKeydown as EventListener);

	function register(shortcut: string, callback: ShortcutCallback, options: ShortcutOptions = {}) {
		const binding: Binding = {
			parsed: parseShortcut(shortcut),
			callback,
			options: {
				...DEFAULT_OPTIONS,
				...options
			}
		};

		bindings.push(binding);

		return () => {
			const index = bindings.indexOf(binding);
			if (index !== -1) bindings.splice(index, 1);
		};
	}

	function destroy() {
		bindings.length = 0;
		eventTarget.removeEventListener('keydown', onKeydown as EventListener);
	}

	return { register, destroy };
}
