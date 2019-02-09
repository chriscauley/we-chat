import React from 'react'

const USER_REGEXP = /<@([^>]+)>/g

const getMentions = text => {
  const mentions = []
  let m
  do {
    m = USER_REGEXP.exec(text)
    if (m) {
      mentions.push(m[1])
    }
  } while (m)
  return mentions
}

const groupMessages = messages => {
  const groups = []
  let group = {}
  messages.forEach(message => {
    if (group.user !== message.user) {
      group = {
        messages: [],
        user: message.user,
        mentions: [],
      }
      groups.push(group)
    }

    group.messages.push(message)
    group.mentions = group.mentions.concat(getMentions(message.text))
  })
  return groups
}

const applyUsersToGroups = (groups, users) => {
  groups.forEach(group => {
    group.user_obj = users[group.user]
    group.messages.forEach(message => {
      message.children = message.text
        .split(USER_REGEXP)
        .filter(s => s.trim())
        .map((part, ip) => {
          const user = users[part]
          if (user) {
            return (
              <span className="user" key={ip}>
                @{user.name}
              </span>
            )
          }
          return <span key={ip}>{part}</span>
        })
    })
  })
}

export { getMentions, groupMessages, applyUsersToGroups }
