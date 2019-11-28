export const createBalance = (balance) => {
    return (dispatch, getState) => {
        // make async call to database
        dispatch({type: 'ADD_BALANCE',  balance});
    }
};