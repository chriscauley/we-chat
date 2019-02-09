import React from 'react'

import ajax from '../lib/ajax'
import { applyUsersToGroups, groupMessages } from '../lib/message'
import { getUsers } from '../lib/users'

const Message = ({ children, text }) => {
  return <div className="message">{children || text}</div>
}

const MessageGroup = props => {
  const { messages, user, user_obj } = props
  let username = user
  if (user_obj) {
    username = user_obj.name
  }
  return (
    <div className="message-group">
      {username}
      {messages.map(message => (
        <Message {...message} key={message.ts} />
      ))}
    </div>
  )
}

//const USER_REGEXP = /<(.*)>/g

class ChannelDetail extends React.Component {
  static path = '/app/channel/:id/'
  state = {
    message_groups: [],
    channel: {},
  }
  getData() {
    if (this._last_id === this.props.id) {
      return
    }
    this._last_id = this.props.id
    ajax.get(`/api/channel/${this.props.id}/messages/`).then(results => {
      const user_ids = new Set()
      const groups = groupMessages(results.messages)
      groups.forEach(group => {
        group.mentions.forEach(id => user_ids.add(id))
      })
      getUsers([...user_ids]).then(users => {
        applyUsersToGroups(groups, users)
        this.setState({
          channel: results.channel,
          message_groups: groups,
        })
      })
      this.setState({
        channel: results.channel,
        message_groups: groups,
      })
    })
  }
  render() {
    this.getData()
    const { channel, message_groups } = this.state
    return (
      <div>
        <h1>{channel.name}</h1>
        {message_groups.map((g, ig) => (
          <MessageGroup {...g} key={ig} />
        ))}
      </div>
    )
  }
}

export default ChannelDetail
