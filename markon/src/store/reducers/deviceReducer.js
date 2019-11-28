
const initState = {
    balances: [
        {id: '1', balance: '8823121', balancetype: 'Total Expence'},
        {id: '2', balance: '5461516', balancetype: 'Cash on Hand'},
        {id: '3', balance: '4545156', balancetype: 'Net Profit Margin'}
      ]
    }
    
  
  
  const deviceReducer = (state = initState, action) => {
        switch(action.type){
            case 'ADD_DEVICE':
                console.log('add device' , action.device)
        }
        return state;
  }
  
  export default deviceReducer