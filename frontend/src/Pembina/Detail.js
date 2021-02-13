import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import useGlobal from '../Global';

export default function Detail() {
	let { id } = useParams();
	const history = useHistory();
	const [globalState, globalActions] = useGlobal();
	const [data, setData] = useState();

	const getLaporan = () => {
		axios
			.get(`${process.env.REACT_APP_API_URL}/laporan/${id}`, {
				headers: {
					Authorization: 'Bearer ' + globalState.access,
				},
			})
			.then((res) => {
				console.log(res);
				setData(res.data);
			})
			.catch((err) => console.log(err));
	};

	const updateLaporan = () => {
		axios({
			url: `${process.env.REACT_APP_API_URL}/laporan/update/${id}`,
			method: 'put',
			headers: {
				Authorization: 'Bearer ' + globalState.access,
			},
		})
			.then((res) => getLaporan())
			.catch((err) => console.log(err));
	};

	const laporPusat = () => {
		axios({
			url: `${process.env.REACT_APP_API_URL}/laporan/lapor_pusat/${id}`,
			method: 'put',
			headers: {
				Authorization: 'Bearer ' + globalState.access,
			},
		})
			.then((res) => getLaporan())
			.catch((err) => console.log(err));
	};

	useEffect(() => {
		if (!localStorage.getItem('santri-token') || !globalState.user.is_staff) {
			localStorage.removeItem('santri-token');
			globalActions.removeToken();
			history.push('/pembina/');
		}
		getLaporan();
	}, []);

	const dateString = (s) => {
		let d = new Date(s);
		return d.toLocaleDateString('id-ID', {
			weekday: 'long',
			year: 'numeric',
			month: 'long',
			day: 'numeric',
		});
	};

	return data ? (
		<div className="flex flex-col text-center	my-12">
			<span className="text-2xl my-2">Detail Laporan</span>
			<span className="pt">Daftar laporan untuk penindakan lebih lanjut</span>

			<table className="table-fixed w-6/12 mx-auto my-6 text-left detail-table">
				<tr>
					<td>Nama</td>
					<td>{data.dilaporkan.nama}</td>
				</tr>
				<tr>
					<td>Nomor Induk</td>
					<td>{data.dilaporkan.nomor_induk}</td>
				</tr>
				<tr>
					<td>Keluhan</td>
					<td>{data.keluhan}</td>
				</tr>
				<tr>
					<td>Penyakit Bawaan</td>
					<td>{data.dilaporkan.penyakit_bawaan}</td>
				</tr>
				<tr>
					<td>Status Penanganan</td>
					<td>
						<span
							className={
								data.lapor_pusat
									? 'text-main'
									: data.status_laporan == 'Menunggu penanganan'
									? 'text-warn'
									: 'text-main'
							}
						>
							{data.lapor_pusat ? 'Lapor pusat' : data.status_laporan}
						</span>
					</td>
				</tr>
				<tr>
					<td>No. Telp</td>
					<td>{data.dilaporkan.telepon}</td>
				</tr>
				<tr>
					<td>Alamat Asal</td>
					<td>{data.dilaporkan.alamat}</td>
				</tr>
				<tr>
					<td>Nama Pelapor</td>
					<td>{data.pelapor.nama}</td>
				</tr>
				<tr>
					<td>Waktu Laporan</td>
					<td>{dateString(data.tanggal_laporan)}</td>
				</tr>
			</table>

			<div className="flex justify-around w-6/12 mx-auto">
				<button
					className="gradient-button w-60"
					style={{ alignSelf: 'center' }}
					onClick={
						data.status_laporan == 'Menunggu penanganan' && !data.lapor_pusat
							? updateLaporan
							: undefined
					}
				>
					TELAH DITANGANI
				</button>
				<button
					className="gradient-warn-button w-60"
					style={{ alignSelf: 'center' }}
					onClick={laporPusat}
				>
					LAPOR PUSAT
				</button>
			</div>
		</div>
	) : (
		<></>
	);
}
