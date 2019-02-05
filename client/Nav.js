import React from 'react'
import { Link } from '@reach/router'

import * as screens from './Screens'

const links = [screens.Home, screens.Login]

export default class Nav extends React.Component {
  render() {
    return (
      <div>
        {links.map(screen => (
          <Link to={screen.path} key={screen.path}>
            {screen.name}
          </Link>
        ))}
      </div>
    )
  }
}
