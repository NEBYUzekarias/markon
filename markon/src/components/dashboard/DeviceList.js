import React from 'react'

const DeviceList =(props) => {
    // const {balance , num , balancetype } = props;
    return(  
<div className="row">
                    
                    <div className="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                        <div className="card">
                            <h5 className="card-header">Device Table</h5>
                            <div className="card-body">
                                <div className="table-responsive">
                                    <table className="table table-striped table-bordered first">
                                        <thead>
                                            <tr>
                                                <th>Name</th>
                                                <th>Status</th>
                                                <th>Serial Number</th>
                                                <th>Number of Maintainance</th>
                                                <th>Age</th>
                                                <th>Acquire date</th>
                                                <th>Price</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>PlayStation 4</td>
                                                <td>Good</td>
                                                <td>154154aF</td>
                                                <td>Nun</td>
                                                <td>61</td>
                                                <td>2011/04/25</td>
                                                <td>$320,800</td>
                                            </tr>
                                            <tr>
                                                <td>PlayStation 4</td>
                                                <td>Good</td>
                                                <td>154154aF</td>
                                                <td>Nun</td>
                                                <td>61</td>
                                                <td>2011/04/25</td>
                                                <td>$320,800</td>
                                            </tr>
                                            <tr>
                                                <td>PlayStation 4</td>
                                                <td>Good</td>
                                                <td>154154aF</td>
                                                <td>Nun</td>
                                                <td>61</td>
                                                <td>2011/04/25</td>
                                                <td>$320,800</td>
                                            </tr>
                                            <tr>
                                                <td>PlayStation 4</td>
                                                <td>Good</td>
                                                <td>154154aF</td>
                                                <td>Nun</td>
                                                <td>61</td>
                                                <td>2011/04/25</td>
                                                <td>$320,800</td>
                                            </tr>
                                            
                                            
                                        </tbody>
                                        <tfoot>
                                            <tr>
                                                <th>Name</th>
                                                <th>Status</th>
                                                <th>Serial Number</th>
                                                <th>Number of Maintainance</th>
                                                <th>Age</th>
                                                <th>Acquire date</th>
                                                <th>Price</th>
                                            </tr>
                                        </tfoot>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                </div>

    )
}

export default DeviceList;