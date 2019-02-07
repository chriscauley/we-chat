import gql from 'graphql-tag'

export const user = gql`
  {
    user {
      id
      email
      username
    }
  }
`
