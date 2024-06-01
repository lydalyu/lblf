import { createSlice } from '@reduxjs/toolkit'


export const userDataSlice = createSlice({
    name: 'userData',
    initialState: {
        value: {},
    },
    reducers: {        
        assign: (state, action) => {
            state.value = action.payload
        },
    },
})

export const { assign } = counterSlice.actions

export const selectUseData = (state) => state.userData.value

export default userDataSlice.reducer
