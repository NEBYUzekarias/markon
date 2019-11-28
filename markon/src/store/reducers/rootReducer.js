import authReducer from './authReducer'
import balanceReducer from './balanceReducer'
import { combineReducers } from 'redux'

const rootReducer = combineReducers({
  auth: authReducer,
  balance: balanceReducer
});

export default rootReducer


