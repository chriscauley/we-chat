import { ApolloProvider } from 'react-apollo'
import React from 'react'
import { render } from 'react-dom'

import client from './graphql/client'
import Nav from './Nav'
import Screens from './Screens'

class Root extends React.Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <div id="Root">
          <Nav />
          <Screens />
        </div>
      </ApolloProvider>
    )
  }
}

const root = document.getElementById('root')
render(<Root />, root)
