const esbuild = require("esbuild");
const fs = require('fs');
const path = require('path');
const production = process.argv.includes('--production');
const watch = process.argv.includes('--watch');

/**
 * @type {import('esbuild').Plugin}
 */
const esbuildProblemMatcherPlugin = {
	name: 'esbuild-problem-matcher',

	setup(build) {
		build.onStart(() => {
			console.log('[watch] build started');
		});
		build.onEnd((result) => {
			result.errors.forEach(({ text, location }) => {
				console.error(`✘ [ERROR] ${text}`);
				console.error(`    ${location.file}:${location.line}:${location.column}:`);
			});
			console.log('[watch] build finished');
		});
	},
};

// Custom function to copy config.json file to dist folder
async function copyConfigFile() {
	const srcPath = path.join(__dirname, 'vscode-client', 'src', 'config.json');
	const destPath = path.join(__dirname, 'dist', 'config.json');

	// If the config.json exists in destPath, do not copy it again
	if (fs.existsSync(destPath)) {
		return;
	}

	return new Promise((resolve, reject) => {
		fs.copyFile(srcPath, destPath, (err) => {
			if (err) {
				console.error('Error copying config.json:', err);
				return reject(err);
			}
			console.log('config.json successfully copied to dist folder');
			resolve();
		});
	});
}

async function main() {
	const ctx = await esbuild.context({
		entryPoints: [
			'vscode-client/src/extension.ts'
		],
		bundle: true,
		format: 'cjs',
		minify: production,
		sourcemap: !production,
		sourcesContent: false,
		platform: 'node',
		outfile: 'dist/extension.js',
		external: ['vscode'],
		logLevel: 'silent',
		plugins: [
			/* add to the end of plugins array */
			esbuildProblemMatcherPlugin,
		],
	});
	if (watch) {
		await ctx.watch();
	} else {
		await ctx.rebuild();
		copyConfigFile();
		await ctx.dispose();
	}
}

main().catch(e => {
	console.error(e);
	process.exit(1);
});
