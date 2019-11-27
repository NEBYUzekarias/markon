import React from 'react';
import Dashboard from './components/dashboard/Dashboard'
import {BrowserRouter , Switch , Route} from 'react-router-dom'
import Navbar from './components/layout/Navbar'
import SignUp from './components/auth/SignUp'
import SignIn from './components/auth/SignIn'




function App() {
  return (
    <div className="App">
    <BrowserRouter>
      <div className="dashboard-main-wrapper">
        <Navbar/>
        <Switch>
          <Route exact path='/' component={Dashboard}/>
          <Route path ='/signup' component ={ SignUp}/>
          <Route path ='/signin' component ={SignIn} />
        </Switch>
      </div>
    </BrowserRouter>
    </div>
  );
}

export default App;
