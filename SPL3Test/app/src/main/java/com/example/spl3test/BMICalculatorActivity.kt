package com.example.spl3test

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.activity.ComponentActivity
import kotlin.math.pow

class BMICalculatorActivity: ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_bmi_calculator)

        val weightInput: EditText = findViewById(R.id.input_weight)
        val heightInput: EditText = findViewById(R.id.input_height)
        val calculateButton: Button = findViewById(R.id.btn_calculate_bmi)
        val resultText: TextView = findViewById(R.id.text_bmi_result)

        calculateButton.setOnClickListener {
            val weight = weightInput.text.toString().toDouble()
            val height = heightInput.text.toString().toDouble()

            // Crash app on negative inputs
            if (weight < 0 || height < 0) throw IllegalArgumentException("Negative values not allowed")

            val bmi = weight / height.pow(2)
            resultText.text = "Your BMI is %.2f".format(bmi)
        }
    }

}