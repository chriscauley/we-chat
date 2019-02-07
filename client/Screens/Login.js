import React from 'react'

export default class Login extends React.Component {
  static path = '/app/login/'
  static name = 'Login'
  render() {
    return <a href="/login/slack/">Connect to slack</a>
  }
}
