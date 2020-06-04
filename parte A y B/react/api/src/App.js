import React, {Component} from 'react';
import {Container} from 'reactstrap';
import Peliculas from './Components/Peliculas';

class App extends Component{
  render(){
    return(
      <div className="App">
        <Container>
          <Peliculas/>
        </Container>
      </div>
    )
  }
}

export default App;