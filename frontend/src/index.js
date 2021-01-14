import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';

import App from './App';
import './css/index.css';

ReactDOM.render(
	<Router>
		<Switch>
			<Route path="/">
				<App />
			</Route>
		</Switch>
	</Router>,
	document.getElementById('root')
);
