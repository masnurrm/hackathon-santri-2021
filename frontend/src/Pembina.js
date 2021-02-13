import React from 'react';
import { Switch, Route, useRouteMatch } from 'react-router-dom';

import Header from './Header/header-pembina';

import Detail from './Pembina/Detail';
import Laporan from './Pembina/Laporan';
import Login from './Pembina/Login';
import Pengaduan from './Pembina/Pengaduan';
import Pengaturan from './Pembina/Pengaturan';
import Tentang from './Tentang';

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
				<Route path={`${path}/pengaduan`}>
					<Pengaduan />
				</Route>
				<Route path={`${path}/pengaturan`}>
					<Pengaturan />
				</Route>
				<Route path={`${path}/tentang`}>
					<Tentang />
				</Route>
				<Route path={`${path}/detail/:id`}>
					<Detail />
				</Route>
			</Switch>
		</>
	);
}
