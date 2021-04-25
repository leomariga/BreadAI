import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import {Recipe} from "./components/Recipe"
import {Sad_backer} from "./components/Sad_backer"
import { Container, Header } from 'semantic-ui-react'

function App() {
  const [recipe, setRecipe] = useState([])

  useEffect(() => {
    fetch('/generate').then(response => 
      response.json().then(data => {
        setRecipe(data.recipe)
        console.log(data.recipe);
      })
      )
  }, [])
  return (
    <div className="App">
      <Container text>
        <Sad_backer />
        <Recipe recipe={recipe} />
      </Container>
      
    </div>
  );
}

export default App;
