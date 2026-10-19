// The <connections-apps> custom element from @cnct/connect (loaded in main.tsx).
import 'react'

declare module 'react' {
  namespace JSX {
    interface IntrinsicElements {
      'connections-apps': React.DetailedHTMLProps<React.HTMLAttributes<HTMLElement>, HTMLElement> & {
        'signed-in'?: string
        current?: string
        'sign-in-href'?: string
        theme?: string
      }
    }
  }
}
