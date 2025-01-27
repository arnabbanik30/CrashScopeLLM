package com.example.spl3test

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.activity.ComponentActivity
import kotlin.math.sqrt

class SquareRootActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sqrt_calculator)

        val numberInput: EditText = findViewById(R.id.input_number)
        val calculateButton: Button = findViewById(R.id.btn_calculate_sqrt)
        val resultText: TextView = findViewById(R.id.text_sqrt_result)

        calculateButton.setOnClickListener {
            val number = numberInput.text.toString().toDouble()

            // Crash app on negative inputs
            if (number < 0) throw IllegalArgumentException("Negative values not allowed")

            val sqrtResult = sqrt(number)
            resultText.text = "Square root: %.2f".format(sqrtResult)
        }
    }
}