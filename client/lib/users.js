import _ from 'lodash'

import { get } from './ajax'

const CACHE = {}

const getUsers = ids => {
  const needed = ids.filter(id => !CACHE[id])
  if (!needed.length) {
    // cache already satified. proceed.
    return Promise.resolve(_.pick(CACHE, ids))
  }
  return get('/api/user/', { user_ids: needed.join(',') }).then(({ users }) => {
    users.forEach(u => {
      CACHE[u.id] = u
    })
    return _.pick(CACHE, ids)
  })
}

export default {
  getUsers,
}
export { getUsers }
