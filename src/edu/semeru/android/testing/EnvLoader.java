package edu.semeru.android.testing;

import java.io.FileNotFoundException;

import org.eclipse.jdt.core.dom.ThisExpression;

import io.github.cdimascio.dotenv.*;

public class EnvLoader {

	private Dotenv dotenv;
	public EnvLoader() {
		try {
			dotenv = Dotenv.load();
		}
		catch (DotenvException e) {
			throw new DotenvException("No .env file found in the root of the project directory. "
					+ "Copy and rename the .env.example file and make necessary edits.");
		}
		catch (Exception e) {
			throw e;
		}
	}
	
	private String getKeyValue(String key, String exceptionMsg) throws Exception{
		String valueString = dotenv.get(key);
		if (valueString == null) {
			throw new Exception(exceptionMsg);
		}
		return valueString;
	}
	
	public String getApkFile() throws Exception {
		return getKeyValue("APK_FILE", 
				"No APK_FILE key found in the .env FILE");
	}
	
	public String getAaptPath() throws Exception {
		return getKeyValue("AAPT_PATH", 
				"No AAPT_PATH key found in the .env FILE");
	}
	
	public String getDataFolder() throws Exception {
		return getKeyValue("DATA_FOLDER", 
				"No DATA_FOLDER key found in the .env FILE");
	}
	public String getScriptsPath() throws Exception {
		return getKeyValue("SCRIPTS_PATH", 
				"No SCRIPTS_PATH key found in the .env FILE");
	}
	public String getAndroidSdkPath() throws Exception {
		return getKeyValue("ANDROID_SDK_PATH", 
				"No ANDROID_SDK_PATH key found in the .env FILE");
	}
	public String getAvdPort() throws Exception {
		return getKeyValue("AVD_PORT", 
				"No AVD_PORT key found in the .env FILE");
	}
	public String getAbdPort() throws Exception {
		return getKeyValue("ABD_PORT", 
				"No ABD_PORT key found in the .env FILE");
	}
	
}
