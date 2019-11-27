import React from 'react'

const Budgets =(props) => {
    const {balance , budget , balancetype , style } = props;
    return(   
       
           <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-12">              
                
                    <div class="card">
                        <h5 class="card-header">% of {balancetype} Budget</h5>
                        <div class="card-body">
                            <div id={style} style={{height: '272px'}}></div>
                        </div>
                        <div class="card-footer bg-white">
                            <p>Budget <span class="float-right text-dark">{budget}</span></p>
                            <p>Balance<span class="float-right text-dark">{balance} <span class="ml-2 text-secondary"><i class="fas fa-caret-up mr-1"></i>25%</span></span>
                            </p>
                        </div>
                    </div>
            </div>
                    
    )
}


export default Budgets 