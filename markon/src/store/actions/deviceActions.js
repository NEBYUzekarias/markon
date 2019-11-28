export const addDevice = (device) =>{
    return(dispatch, getState , {getFirebase , getFirestore}) =>{
       // make async call to database
       const firestore = getFirestore();
       const profile = getState().firebase.profile;
       const authorId = getState().firebase.auth.uid;
       firestore.collection('devices').add({
           ...device, 
           authorFirstName: profile.firstName,
           authorLastName: profile.lastName,
           authorId: authorId,
           createdAt: new Date()
       }).then(() => {
        dispatch({type: 'ADD_DEVICE', device}); 
       }).catch((err) => {
           dispatch({type: 'ADD_DEVICE_ERROR', err});
       })
       
    }
};