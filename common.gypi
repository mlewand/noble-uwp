{
	'variables' : {
		'node_shared': 'true',
		'WIN_VER' : 'v10',
		'WIN_SDK_VER' : '10.0.15063.0',
		'VS_VER': '14.0',
	},
	'target_defaults': {
		'default_configuration': 'Release',
		'configurations': {
			'Debug': {
				'msvs_settings': {
					'VCCLCompilerTool': {
						'RuntimeLibrary': '3', # /MDd
					}
				}
			},
			'Release': {
				'msvs_settings': {
					'VCCLCompilerTool': {
						'RuntimeLibrary': '2', # /MD
					}
				}
			}
		},
		'msvs_settings': {
			'VCCLCompilerTool': {
				'AdditionalOptions': [ '/ZW'],
				'AdditionalUsingDirectories' : [
					'%ProgramFiles(x86)%/Microsoft Visual Studio <(VS_VER)/VC/lib/store/references',
					'%ProgramFiles%/Microsoft Visual Studio <(VS_VER)/VC/lib/store/references',
					'%ProgramFiles(x86)%/Windows Kits/10/UnionMetadata/<(WIN_SDK_VER)',
					'%ProgramFiles%/Windows Kits/10/UnionMetadata/<(WIN_SDK_VER)',
					# An ugly workaround to make it work with vs build tools rather than full blown vs 🤷‍♂️
					'%ProgramFiles(x86)%/Microsoft Visual Studio/2017/BuildTools/VC/Tools/MSVC/14.16.27023/lib/x86/store/references',
					'%ProgramFiles%/Microsoft Visual Studio/2017/BuildTools/VC/Tools/MSVC/14.16.27023/lib/x86/store/references',
				],
				'ExceptionHandling': 1, # /EHsc
			}
		}
	}
}
