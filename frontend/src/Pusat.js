import React from 'react';
import { Switch, Route, useRouteMatch } from 'react-router-dom';

import Header from './Header/header-pusat';

import Detail from './Pusat/Detail';
import Laporan from './Pusat/Laporan';
import Login from './Pusat/Login';

export default function Pembina() {
	let { url, path } = useRouteMatch();
	return (
		<>
			<Header />
			<Switch>
				<Route exact path={path}>
					<Login />
				</Route>
				<Route path={`${path}/laporan`}>
					<Laporan />
				</Route>
				<Route path={`${path}/detail/:id`}>
					<Detail />
				</Route>
			</Switch>
		</>
	);
}
