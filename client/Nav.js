import React from 'react'
import { Link } from '@reach/router'
import { graphql } from 'react-apollo'

import { user } from './graphql/user'
import * as screens from './Screens'

const links = [screens.Home, screens.Login]

class Nav extends React.Component {
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

export default graphql(user, {})(Nav)
