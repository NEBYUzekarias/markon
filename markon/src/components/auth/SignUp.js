import React, { Component } from 'react'



class SignUp extends Component {

    render() {
        
        return (
            <div>            
                <form className="splash-container">
                    <div className="card">
                        <div className="card-header">
                            <h3 className="mb-1">Registrations Form</h3>
                            <p>Please enter your user information.</p>
                        </div>
                        <div className="card-body">
                            <div className="form-group">
                                <input className="form-control form-control-lg" type="text" name="nick" required="" placeholder="Username" autocomplete="off"/>
                            </div>
                            <div className="form-group">
                                <input className="form-control form-control-lg" type="email" name="email" required="" placeholder="E-mail" autocomplete="off"/>
                            </div>
                            <div className="form-group">
                                <input className="form-control form-control-lg" id="pass1" type="password" required="" placeholder="Password"/>
                            </div>
                            <div className="form-group">
                                <input className="form-control form-control-lg" required="" placeholder="Confirm"/>
                            </div>
                            <div className="form-group pt-2">
                                <button className="btn btn-block btn-primary" type="submit">Register My Account</button>
                            </div>
                            <div className="form-group">
                                <label className="custom-control custom-checkbox">
                                    <input className="custom-control-input" type="checkbox"/><span className="custom-control-label">By creating an account, you agree the <a href="#">terms and conditions</a></span>
                                </label>
                            </div>
                            <div className="form-group row pt-0">
                                <div className="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 mb-2">
                                    <button className="btn btn-block btn-social btn-facebook " type="button">Facebook</button>
                                </div>
                                <div className="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                                    <button className="btn  btn-block btn-social btn-twitter" type="button">Twitter</button>
                                </div>
                            </div>
                        </div>
                        <div className="card-footer bg-white">
                            <p>Already member? <a href="#" className="text-secondary">Login Here.</a></p>
                        </div>
                    </div>
                </form>


            </div>



                )
    }
}


export default  SignUp;