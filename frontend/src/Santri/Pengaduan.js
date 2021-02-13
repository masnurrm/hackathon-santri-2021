import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useForm } from 'react-hook-form';
import useGlobal from '../Global';

export default function Pengaduan() {
	const { register, handleSubmit } = useForm();
	const [globalState, globalActions] = useGlobal();
	const [status, setStatus] = useState('');

	const sendMsg = () => {};

	return (
		<form
			className="flex flex-col text-center	my-12 items-center max-w-4xl mx-auto"
			onSubmit={handleSubmit(sendMsg)}
		>
			<span className="text-2xl my-2">Pengaduan</span>
			<span className="pt mb-6">
				Kolom pengaduan layanan atau lupa kata sandi
			</span>

			<div className="form w-4/12 flex flex-col my-auto">
				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-account-outline text-gray-400 text-lg"></i>
					</div>
					<input type="text" class="input-text" placeholder="Nomor Induk" />
				</div>

				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-key-outline text-gray-400 text-lg"></i>
					</div>
					<input type="text" class="input-text" placeholder="Email" />
				</div>

				<div class="flex my-2">
					<div class="input-icon self-start my-2">
						<i class="mdi mdi-email-outline text-gray-400 text-lg"></i>
					</div>
					<textarea class="input-text" placeholder="Pesan" height="10" />
				</div>

				<button className="gradient-button my-2">KIRIM</button>
			</div>
		</form>
	);
}
