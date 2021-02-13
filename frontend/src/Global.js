import React from 'react';
import jwt from 'jwt-decode';
import globalHook from 'use-global-hook';

const token = JSON.parse(localStorage.getItem('santri-token'));

const initialState = {
	isLoggedIn: token ? true : false,
	refresh: token && token.refresh,
	access: token && token.access,
	user: token && jwt(token.access).user,
};

const actions = {
	setToken: (store, token) => {
		store.setState({
			isLoggedIn: true,
			refresh: token.refresh,
			access: token.access,
			user: jwt(token.access).user,
		});
	},
	removeToken: (store) => {
		store.setState({
			isLoggedIn: false,
			refresh: null,
			access: null,
			user: null,
		});
	},
};

const useGlobal = globalHook(React, initialState, actions);

export default useGlobal;
