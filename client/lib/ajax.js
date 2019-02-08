import cookie from 'cookie'
import queryString from 'query-string'

export const post = (url, formData, headers = {}) => {
  return fetch(url, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'X-CSRFToken': cookie.parse(document.cookie).csrftoken,
      ...headers,
    },
    body: JSON.stringify(formData),
  })
}

export const get = (url, params) => {
  if (params) {
    url += '?' + queryString.stringify(params)
  }
  return fetch(url).then(r => r.json())
}

export default {
  post,
  get,
}
