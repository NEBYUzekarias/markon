import React from 'react'


const Balance =(props) => {
    const {balance , num , balancetype } = props;
    return(                        
    <div className="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-12">     
            <div className="card">
                    <h5 className="card-header">{balancetype}</h5>
                    <div className="card-body">
                        <div className="metric-value d-inline-block">
                            <h1 className="mb-1">{balance}</h1>
                        </div>
                        <div className="metric-label d-inline-block float-right text-secondary font-weight-bold">
                            <span className="icon-circle-small icon-box-xs text-danger bg-danger-light"><i className="fa fa-fw fa-arrow-down"></i></span><span className="ml-1">15%</span>
                        </div>
                    </div>
                    <div className="card-body text-center bg-light p-t-40 p-b-40">
                        <div id={"sparkline-revenue" + num}></div>
                    </div>
                    <div className="card-footer text-center bg-white">
                        <a href="#" className="card-link">View Details</a>
                    </div>
            </div>
    </div>
    )
}


export default Balance;
                        