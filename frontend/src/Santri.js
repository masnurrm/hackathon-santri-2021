import React from 'react';
import { Switch, Route } from 'react-router-dom';

import Detail from './Santri/Detail';
import Header from './Header/header';
import Laporan from './Santri/Laporan';
import Login from './Santri/Login';
import Pengaduan from './Santri/Pengaduan';
import Pengaturan from './Santri/Pengaturan';
import Status from './Santri/Status';
import Tentang from './Tentang';
import Sandi from './Santri/Sandi';
import Reset from './Santri/Reset';

import useGlobal from './Global';

export default function Santri() {
	const [global, setGlobal] = useGlobal();

	return (
		<>
			<Header />
			<Switch>
				<Route exact path="/">
					<Login />
				</Route>
				<Route path="/laporan">
					<Laporan />
				</Route>
				<Route path="/pengaduan">
					<Pengaduan />
				</Route>
				<Route path="/pengaturan">
					<Pengaturan />
				</Route>
				<Route path="/status">
					<Status />
				</Route>
				<Route path="/tentang">
					<Tentang />
				</Route>
				<Route path="/lupa-sandi">
					<Sandi />
				</Route>
				<Route path="/reset/:uid/token/:token">
					<Reset />
				</Route>
				<Route path="/detail/:id">
					<Detail />
				</Route>
			</Switch>
		</>
	);
}
