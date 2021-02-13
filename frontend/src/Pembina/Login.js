import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link, useHistory } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import useGlobal from '../Global';

export default function Login() {
	const { register, handleSubmit } = useForm();
	const history = useHistory();

	const [globalState, globalActions] = useGlobal();
	const [isLoading, setLoading] = useState(false);
	const [status, setStatus] = useState('');

	const login = (data) => {
		setLoading(true);

		axios
			.post(`${process.env.REACT_APP_API_URL}/token/`, {
				nomor_induk: data.nomor_induk,
				password: data.password,
			})
			.then((res) => {
				localStorage.setItem('santri-token', JSON.stringify(res.data));
				globalActions.setToken(res.data);

				setLoading(false);
			})
			.catch((err) => {
				console.log(err);
				setStatus('Terjadi kesalahan');
				setLoading(false);
			});
	};

	return isLoading ? (
		<p className="text-3xl mx-auto my-20 text-center">Loading....</p>
	) : (
		<div className="flex max-w-5xl mx-auto">
			<img src="/Santri.png" alt="santri" className="w-6/12" />
			<span className="w-1/12"></span>
			{globalState.isLoggedIn ? (
				<div className="pt-40 flex flex-col">
					<p className="text-gray-600 text-3xl my-2">
						Selamat datang, {globalState.user.nama}
					</p>
					<p className="pt">Lihat daftar laporan para santri di sini</p>
					<Link
						className="gradient-button mt-4 text-center"
						to="/pembina/laporan"
						type="submit"
					>
						LAPORAN
					</Link>
				</div>
			) : (
				<form
					className="form w-4/12 flex flex-col my-auto"
					onSubmit={handleSubmit(login)}
				>
					<span className="text-gray-600 text-3xl my-2 text-center">
						Pembina Login
					</span>
					<span className="text-warn pt text-center">{status}</span>
					<div class="flex my-2">
						<div class="input-icon">
							<i class="mdi mdi-account-outline text-gray-400 text-lg"></i>
						</div>
						<input
							type="text"
							class="input-text"
							ref={register}
							name="nomor_induk"
							placeholder="Nomor Identitas"
						/>
					</div>

					<div class="flex my-2">
						<div class="input-icon">
							<i class="mdi mdi-key-outline text-gray-400 text-lg"></i>
						</div>
						<input
							type="password"
							class="input-text"
							ref={register}
							name="password"
							placeholder="Kata Sandi"
						/>
					</div>

					<button className="gradient-button my-2" type="submit">
						LOGIN
					</button>

					<span className="pt text-center">
						Silahkan klik{' '}
						<Link className="text-main" to="/lupa-sandi">
							link ini
						</Link>{' '}
						apabila lupa kata sandi
					</span>
				</form>
			)}
		</div>
	);
}
