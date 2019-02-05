import { ApolloProvider } from 'react-apollo'
import React from 'react'
import { render } from 'react-dom'

import client from './graphql/client'

class Root extends React.Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <div>yay</div>
      </ApolloProvider>
    )
  }
}

const root = document.getElementById('root')
render(<Root />, root)
