
const initState = {
  balances: [
      {id: '1', balance: '8823121', balancetype: 'Total Expence'},
      {id: '2', balance: '5461516', balancetype: 'Cash on Hand'},
      {id: '3', balance: '4545156', balancetype: 'Net Profit Margin'}
    ]
  }
  


const balanceReducer = (state = initState, action) => {
  return state;
}

export default balanceReducer