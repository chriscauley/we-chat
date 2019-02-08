import _ from 'lodash'
import React from 'react'
import { Link } from '@reach/router'
import { graphql } from 'react-apollo'

import { get } from './lib/ajax'
import { user } from './graphql/user'
import * as screens from './Screens'

const links = [screens.Home, screens.Login]

class ChannelList extends React.Component {
  render() {
    const { channels } = this.props
    return (
      <div className="nav">
        {channels.map(({ id, name }) => (
          <Link to={`/app/channel/${id}/`} key={id}>
            {name}
          </Link>
        ))}
      </div>
    )
  }
}

class Nav extends React.Component {
  state = {
    channels: [],
  }
  componentDidMount() {
    get('/api/channel/').then(({ results }) => {
      results = _.sortBy(results, 'name')
      this.setState({ channels: results })
    })
  }
  render() {
    return (
      <div id="nav">
        <div className="nav">
          {links.map(screen => (
            <Link to={screen.path} key={screen.path} className="nav-item">
              {screen.name}
            </Link>
          ))}
        </div>
        <div className="divider" />
        <ChannelList channels={this.state.channels} />
      </div>
    )
  }
}

export default graphql(user, {})(Nav)
