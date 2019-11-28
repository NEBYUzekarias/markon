import React, { Component } from 'react'
import Balance from './Balance'
import Sidebar from './Sidebar'
import Budgets from './Budgets'
import DeviceList from './DeviceList'
import { connect } from 'react-redux'


class Dashboard extends Component {
  render() {
    console.log(this.props)
    const {balances} = this.props

    const balanceList = balances.length ? (
        balances.map(balance => {
          return (
            
            <Balance balance = {balance.balance}  num={balance.id} balancetype={balance.balancetype} key={balance.id}/>
          )
        })
      ) : (
        <div className="center">No posts to show</div>
      );

        return (
        
        <div>
            <Sidebar/>
        
            <div className="dashboard-wrapper">
                <div className="dashboard-finance">
                    <div className="container-fluid dashboard-content">
                        {/* <!-- ============================================================== -->
                        <!-- pageheader  -->
                        <!-- ============================================================== --> */}
                        <div className="row">
                            <div className="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                                <div className="page-header">
                                    <h3 className="mb-2">Markon Dashboard </h3>
                                    <div className="page-breadcrumb">
                                        <nav aria-label="breadcrumb">
                                            <ol className="breadcrumb">
                                                <li className="breadcrumb-item"><a href="#" className="breadcrumb-link">Dashboard</a></li>
                                                <li className="breadcrumb-item active" aria-current="page">Markon Dashboard </li>
                                            </ol>
                                        </nav>
                                    </div>
                                </div>
                            </div>
                        </div>
                        {/* <!-- ============================================================== -->
                        <!-- end pageheader  -->
                        <!-- ============================================================== -->*/}
                        <div className="row"> 
                            <div className="offset-xl-10 col-xl-2 col-lg-2 col-md-6 col-sm-12 col-12">
                                <form>
                                    <div className="form-group">
                                        <input className="form-control" type="text" name="daterange" value="01/01/2018 - 01/15/2018" />
                                    </div>
                                </form>
                            </div>
                        </div>
                        <div className="row">
                            
                                {balanceList}
                                <Budgets balance = {79464}  budget={12000.00} balancetype={"Income"} style={"morris_gross"}/>
                                <Budgets balance = {79464}  budget={3} balancetype={"Expenses" } style={"morris_profit"}/>
                        </div>
                        
                        <DeviceList/>
                        
                                
                            
                    
                        
                    </div>

            </div>
        </div>
        </div>      

    )
  }
}

const mapStateToProps = (state) =>{
    return{
        balances: state.balance.balances
    }

}


export default connect(mapStateToProps)(Dashboard)