import React from 'react'

import { get } from '../lib/ajax'

const ChannelMessage = ({ text }) => {
  return <div>{text}</div>
}

//const USER_REGEXP = /<(.*)>/g

class ChannelDetail extends React.Component {
  static path = '/app/channel/:id/'
  state = {
    messages: [],
    channel: {},
  }
  getData() {
    if (this._last_id === this.props.id) {
      return
    }
    this._last_id = this.props.id
    get(`/api/channel/${this.props.id}/messages/`).then(results => {
      /*results.messages.forEach(result => {
        result.text.match(USER_REGEXP)
      })*/
      this.setState(results)
    })
  }
  render() {
    this.getData()
    const { channel, messages } = this.state
    return (
      <div>
        <h1>{channel.name}</h1>
        {messages.map(m => (
          <ChannelMessage {...m} key={m.id} />
        ))}
      </div>
    )
  }
}

export default ChannelDetail
