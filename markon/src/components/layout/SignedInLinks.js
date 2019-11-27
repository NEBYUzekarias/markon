import React from 'react'
import {NavLink } from 'react-router-dom'

const SignedInLinks =() => {
    
    return(
        <ul className="right">
            <li><NavLink to='/create'>New Project</NavLink></li>
            <li><a onClick="{props.signOut}">Log Out</a></li>
            <li><NavLink to='/' className='btn btn-floating pink lighten-1'>
               Bla
            </NavLink></li>
            
        </ul>
    )
}




export default SignedInLinks;