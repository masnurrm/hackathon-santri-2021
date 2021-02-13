import React, { useState, useEffect } from 'react';
import { Link, useHistory } from 'react-router-dom';
import axios from 'axios';
import useGlobal from '../Global';
import { useForm } from 'react-hook-form';

export default function Laporan() {
	const [globalState, globalActions] = useGlobal();
	const [warning, setWarning] = useState(false);
	const { register, handleSubmit } = useForm();
	const history = useHistory();

	const lapor = (data) => {
		let { nomor_induk, keluhan } = data;

		if (!nomor_induk || !keluhan) {
			setWarning(true);
			return;
		} else {
			setWarning(false);
		}

		axios
			.post(
				`${process.env.REACT_APP_API_URL}/laporan/`,
				{
					dilaporkan: nomor_induk,
					keluhan,
				},
				{
					headers: {
						Authorization: 'Bearer ' + globalState.access,
					},
				}
			)
			.then((res) => {
				console.log(res);
				history.push('/status');
			})
			.catch((err) => {
				console.log(err);
			});
	};

	useEffect(() => {
		if (!localStorage.getItem('santri-token')) {
			history.push('/');
		}
	}, []);

	return (
		<form
			className="max-w-5xl mt-16 mx-auto text-center flex flex-col "
			onSubmit={handleSubmit(lapor)}
		>
			<span className="text-4xl">
				Assalamualaikum,{' '}
				<span className="text-main">{globalState?.user?.nama}</span>
			</span>
			<span className=" border-b-2 border-main w-4/5 mx-auto">&nbsp;</span>

			<div className="lapor flex my-6 w-4/5 mx-auto">
				<div className="form w-5/12">
					<span className="text-3xl">Lapor Kesehatan Santri</span>
					<br></br>

					{warning && (
						<span className="text-warn pt">
							Mohon isi semua data terlebih dahulu
						</span>
					)}

					{/*<div className="flex my-4">
						<div className="input-icon">
							<i className="mdi mdi-account-outline text-gray-400 text-lg"></i>
						</div>
						<input
							type="text"
							className="input-text"
							placeholder="Nama Lengkap"
						/>
					</div>*/}

					<div className="flex my-4">
						<div className="input-icon">
							<i className="mdi mdi-key-outline text-gray-400 text-lg"></i>
						</div>
						<input
							type="text"
							name="nomor_induk"
							className="input-text"
							placeholder="Nomor Induk"
							ref={register}
						/>
					</div>

					<div className="flex my-4">
						<div className="input-icon">
							<i className="mdi mdi-hospital-box-outline text-gray-400 text-lg"></i>
						</div>
						<input
							type="text"
							className="input-text"
							placeholder="Keluhan"
							name="keluhan"
							ref={register}
						/>
					</div>

					<span className="text-xl pt">Pastikan keluhan tidak salah!!</span>
				</div>

				<span className="w-2/12"></span>

				<div className="status w-5/12 ">
					<span className="text-3xl">Status Laporan Santri</span>
					<p className="pt text-left my-2 text-lg">
						Lihat dan cek status laporan yang telah Anda lakukan untuk
						mengetahui status penanganan kesehatan saat ini!
					</p>
				</div>
			</div>

			<div className="flex w-4/5 mx-auto">
				<button className="gradient-button w-5/12" type="submit">
					LAPOR
				</button>
				<span className="w-2/12"></span>
				<Link to="/status" className="gradient-button w-5/12" type="button">
					STATUS LAPORAN
				</Link>
			</div>
		</form>
	);
}
