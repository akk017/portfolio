export interface Page {
  type: "Page";
  title: string;
  href: string;
  folder: false;
  icon: string;
}

export interface Section {
  type: "Section";
  title: string;
  folder: true;
  children: NavItem[];
}

export type NavItem = Page | Section;

export const navData: NavItem[] = [
  {
    type: "Section",
    title: "algorithmic-trading",
    folder: true,
    children: [
      {
        type: "Page",
        title: "algorithmic trading",
        href: "/algorithmic-trading/trade.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "cses",
    folder: true,
    children: [
      {
        type: "Page",
        title: "cpp tips and tricks",
        href: "/cses/cpp-tips.html",
        folder: false,
        icon: "bookmark"
      },
      {
        type: "Page",
        title: "resource for cses",
        href: "/cses/main.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "data-structures-and-algorithms",
    folder: true,
    children: [
      {
        type: "Section",
        title: "graphs",
        folder: true,
        children: [
          {
            type: "Page",
            title: "a - introduction",
            href: "/data-structures-and-algorithms/graphs/a-introduction.html",
            folder: false,
            icon: "bookmark"
          },
          {
            type: "Page",
            title: "common graph theory problems",
            href: "/data-structures-and-algorithms/graphs/b-common-problems.html",
            folder: false,
            icon: "bookmark"
          },
          {
            type: "Page",
            title: "trees",
            href: "/data-structures-and-algorithms/graphs/c-tress.html",
            folder: false,
            icon: "bookmark"
          },
          {
            type: "Section",
            title: "problems",
            folder: true,
            children: [
              {
                type: "Page",
                title: "a - dungeon master",
                href: "/data-structures-and-algorithms/graphs/problems/a-dugen-master.html",
                folder: false,
                icon: "bookmark"
              },
              {
                type: "Page",
                title: "beginner tree problems",
                href: "/data-structures-and-algorithms/graphs/problems/b-beginner-tree-problems.html",
                folder: false,
                icon: "bookmark"
              },
              {
                type: "Page",
                title: "medium level tree problems",
                href: "/data-structures-and-algorithms/graphs/problems/c-medium-tree-problems.html",
                folder: false,
                icon: "bookmark"
              },
              {
                type: "Page",
                title: "graph isomorphism",
                href: "/data-structures-and-algorithms/graphs/problems/d-graph-isomorphism.html",
                folder: false,
                icon: "bookmark"
              },
              {
                type: "Page",
                title: "lowest common ancestor",
                href: "/data-structures-and-algorithms/graphs/problems/e-lowest-common-ancestor.html",
                folder: false,
                icon: "bookmark"
              },
              {
                type: "Page",
                title: "topological sort",
                href: "/data-structures-and-algorithms/graphs/problems/f-topological-sort-algorithms.html",
                folder: false,
                icon: "bookmark"
              }
            ]
          }
        ]
      },
      {
        type: "Page",
        title: "roadmap",
        href: "/data-structures-and-algorithms/roadmap.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Page",
    title: "daily designer new",
    href: "/ddr.html",
    folder: false,
    icon: "bookmark"
  },
  {
    type: "Section",
    title: "design",
    folder: true,
    children: [
      {
        type: "Page",
        title: "css collection",
        href: "/design/css.html",
        folder: false,
        icon: "bookmark"
      },
      {
        type: "Page",
        title: "fonts",
        href: "/design/fonts.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Page",
    title: "waste land",
    href: "/dump.html",
    folder: false,
    icon: "bookmark"
  },
  {
    type: "Page",
    title: "flow",
    href: "/flow.html",
    folder: false,
    icon: "bookmark"
  },
  {
    type: "Section",
    title: "git",
    folder: true,
    children: [
      {
        type: "Page",
        title: "useful hooks",
        href: "/git/hooks.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "go",
    folder: true,
    children: [
      {
        type: "Section",
        title: "100-mistakes",
        folder: true,
        children: [
          {
            type: "Page",
            title: "mistake 32",
            href: "/go/100-mistakes/mistake-32.html",
            folder: false,
            icon: "bookmark"
          }
        ]
      },
      {
        type: "Page",
        title: "blogs",
        href: "/go/blogs.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "graphic-design",
    folder: true,
    children: [
      {
        type: "Page",
        title: "generative art",
        href: "/graphic-design/generative-art.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "img",
    folder: true,
    children: []
  },
  {
    type: "Page",
    title: "about me",
    href: "/index.html",
    folder: false,
    icon: "bookmark"
  },
  {
    type: "Section",
    title: "kubernetes",
    folder: true,
    children: [
      {
        type: "Page",
        title: "learn k8s",
        href: "/kubernetes/learn-kube.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "mac-os-apps",
    folder: true,
    children: [
      {
        type: "Page",
        title: "apps that i use daily",
        href: "/mac-os-apps/apps.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "mathematics",
    folder: true,
    children: [
      {
        type: "Section",
        title: "combination",
        folder: true,
        children: []
      },
      {
        type: "Section",
        title: "permutation",
        folder: true,
        children: [
          {
            type: "Page",
            title: "materials",
            href: "/mathematics/permutation/a-material.html",
            folder: false,
            icon: "bookmark"
          },
          {
            type: "Page",
            title: "introduction to permuation",
            href: "/mathematics/permutation/b-introduction.html",
            folder: false,
            icon: "bookmark"
          }
        ]
      }
    ]
  },
  {
    type: "Section",
    title: "networking",
    folder: true,
    children: [
      {
        type: "Page",
        title: "networking overview",
        href: "/networking/001-networking-overview.html",
        folder: false,
        icon: "bookmark"
      },
      {
        type: "Page",
        title: "sockets api",
        href: "/networking/002-sockets-api.html",
        folder: false,
        icon: "bookmark"
      },
      {
        type: "Page",
        title: "networking layer model",
        href: "/networking/003-network-layer-model.html",
        folder: false,
        icon: "bookmark"
      },
      {
        type: "Page",
        title: "http server and client",
        href: "/networking/004-http-server-and-client.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "portfolios",
    folder: true,
    children: [
      {
        type: "Page",
        title: "design portfolio",
        href: "/portfolios/design.html",
        folder: false,
        icon: "bookmark"
      },
      {
        type: "Page",
        title: "software devs / cs engineers",
        href: "/portfolios/dev.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "python",
    folder: true,
    children: [
      {
        type: "Page",
        title: "namespaces",
        href: "/python/namespace.html",
        folder: false,
        icon: "bookmark"
      },
      {
        type: "Page",
        title: "peg parge",
        href: "/python/pegparser.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "queue",
    folder: true,
    children: [
      {
        type: "Page",
        title: "read queue",
        href: "/queue/read-queue.html",
        folder: false,
        icon: "bookmark"
      },
      {
        type: "Page",
        title: "watch queue",
        href: "/queue/watch-queue.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "read-takeaways",
    folder: true,
    children: [
      {
        type: "Page",
        title: "tech blogs",
        href: "/read-takeaways/tech.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "self-host",
    folder: true,
    children: [
      {
        type: "Page",
        title: "awesome self host application",
        href: "/self-host/index.html",
        folder: false,
        icon: "bookmark"
      }
    ]
  },
  {
    type: "Section",
    title: "system-design",
    folder: true,
    children: []
  },
  {
    type: "Page",
    title: "todo",
    href: "/todo.html",
    folder: false,
    icon: "bookmark"
  }
];