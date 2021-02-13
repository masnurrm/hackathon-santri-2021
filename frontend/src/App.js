import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Santri from './Santri';
import Pembina from './Pembina';
import Pusat from './Pusat';

export default function App() {
	return (
		<Router>
			<Switch>
				<Route path="/pembina">
					<Pembina />
				</Route>
				<Route path="/pusat">
					<Pusat />
				</Route>
				<Route path="/">
					<Santri />
				</Route>
			</Switch>
		</Router>
	);
}
