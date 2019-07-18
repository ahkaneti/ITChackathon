import React from 'react';
import MainPage from './MainPage';
import Login from './Login';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import './App.css'


function App(){
  return (
    <Router>
      <div className='screen'>
        <Route path="/map" component={MainPage}/>
        <Route path="/login" component={Login} />
      </div>
    </Router>
  );
}

export default App;