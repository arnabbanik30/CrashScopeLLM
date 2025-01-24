package edu.semeru.android.testing;

import java.io.FileNotFoundException;

import org.eclipse.jdt.core.dom.ThisExpression;

import io.github.cdimascio.dotenv.*;

public class EnvLoader {

	private static Dotenv dotenv;
	private static EnvLoader instanceEnvLoader;
	private EnvLoader() {
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
	
	public static Dotenv getDotEnvInstance() {
		if (instanceEnvLoader == null) {
			instanceEnvLoader = new EnvLoader();
		}
		return instanceEnvLoader.getDotenv();
	}
	
	private Dotenv getDotenv() {
		return dotenv;
	}
	
}
