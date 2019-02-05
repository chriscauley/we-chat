import React from 'react'
import { render } from 'react-dom'

class Root extends React.Component {
  render() {
    return (
      <div>yay</div>
    )
  }
}

const root = document.getElementById('root')
render(
  <Root />,
  root,
)