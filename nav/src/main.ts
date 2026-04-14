import { mount } from 'svelte'
import Nav from './nav.svelte'

const app = mount(Nav, {
  target: document.getElementById('nav')!,
})

export default app
