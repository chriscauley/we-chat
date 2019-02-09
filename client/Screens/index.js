import React from 'react'
import { Router } from '@reach/router'

import Home from './Home'
import Login from './Login'
import ChannelDetail from './ChannelDetail'

const raw_screens = [Login, Home, ChannelDetail]

const screens = raw_screens.map((Screen, key) => [
  Screen,
  {
    path: Screen.path,
    key,
  },
])

export { Login, Home, ChannelDetail }

export default class Screens extends React.Component {
  render() {
    return (
      <Router id="Screens">
        {screens.map(([Screen, props]) => (
          <Screen {...props} key={props.key} />
        ))}
      </Router>
    )
  }
}
