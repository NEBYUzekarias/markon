import React, { Component } from 'react'
import { addDevice} from '../../store/actions/deviceActions'
import { connect } from 'react-redux'
import { Redirect } from 'react-router-dom'

class AddDevice extends Component {
    state ={
        name: '',
        serialNumber: '',
        date: '',
        numberOfMaintainance: '',
        deviceStatus:'',
        price: ''
    }
    handleChange = (e) =>{
       this.setState({
        [e.target.id]: e.target.value
       })
    }

    handleSubmit = (e) =>{
        e.preventDefault();
        // console.log(this.state);
        this.props.addDevice(this.state)
        this.props.history.push('/');
    }
    render() {
        // const { auth } = this.props;
        // if (!auth) return <Redirect to ='/signin'/>
        return (
            
            <div className="row center">
                <div className="col-xl-2 col-lg-2 col-md-2 col-sm-0 col-0">
                </div>

                <div className="col-xl-8 col-lg-8 col-md-10 col-sm-12 col-12">
                    <div className="section-block" id="basicform">
                        <h3 className="section-title">Add New Device</h3>
                </div>
                <div className="card">
                        <h5 className="card-header">Device Form</h5>
                            <div className="card-body">
                                <form onSubmit={this.handleSubmit}>
                                            <div className="row">
                                        <div className="col-xl-5 col-lg-5 col-md-5 col-sm-12 col-12">
                                            <div className="form-group">
                                                <label for="inputText3" className="col-form-label">Device Name</label>
                                                <input id="name" type="text" className="form-control" onChange={this.handleChange}/>
                                        
                                                <label for="inputText3" className="col-form-label">Device Status</label>
                                                <input id="deviceStatus" type="text" className="form-control" onChange={this.handleChange}/>
                                                <label for="inputText3" className="col-form-label">Serial Number</label>
                                                <input id="serialNumber" type="text" className="form-control" onChange={this.handleChange}/>
                                            </div>
                                        </div>
                                        <div className="col-xl-5 col-lg-5 col-md-5 col-sm-12 col-12">
                                            <div className="row">
                                                <div className="form-group"></div>
                                                    <label for="inputText4" className="col-form-label">Number Of Maintainance</label>
                                                    <input id="numberOfMaintainance" type="number" className="form-control" placeholder="0" onChange={this.handleChange}/>
                                                    <label>Acquire date <small class="text-muted">dd/mm/yyyy</small></label>
                                                    <input type="date" class="form-control date-inputmask" id="date-mask" placeholder="" onChange={this.handleChange}/>
                                                    <label for="inputText4" className="col-form-label">Price</label>
                                                    <input id="price" type="number" className="form-control" placeholder="0" onChange={this.handleChange}/>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-sm-6 pl-0">
                                            <p class="text-right">
                                                <button type="submit" class="btn btn-space btn-primary">Submit</button>
                                                <button class="btn btn-space btn-secondary">Cancel</button>
                                            </p>
                                        </div>  
                                    </form>
                                </div>
                            
                            </div>
                        </div>
                        
                    <div className="col-xl-2 col-lg-2 col-md-2 col-sm-0 col-0">
            </div>
        </div>
        )
    }
}

// const mapStateToProps = (state) => {
//     return{
//         auth: state.firebase.auth
//     }
// }
const mapDispatchToProps = (dispatch) =>{
    return{
        addDevice: (device) => dispatch(addDevice(device))
    }
}
export default connect(null, mapDispatchToProps)(AddDevice)
