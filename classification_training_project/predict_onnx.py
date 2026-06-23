import onnxruntime as ort
import numpy as np

MODEL_PATH = "student_result_model.onnx"

def load_model():
    session = ort.InferenceSession(
        MODEL_PATH,
        providers=["CPUExecutionProvider"]
    )
    return session

def predict_student(
    session,
    hours_studied,
    attendance_percent,
    previous_marks,
    assignment_score
):
    # Must match training feature order exactly
    input_data = np.array(
        [[
            hours_studied,
            attendance_percent,
            previous_marks,
            assignment_score
        ]],
        dtype=np.float32
    )

    input_name = session.get_inputs()[0].name

    outputs = session.run(
        None,
        {input_name: input_data}
    )

    print("\nRaw Outputs:")
    for i, output in enumerate(outputs):
        print(f"Output {i}: {output}")

    prediction = outputs[0][0]

    print("\nPrediction:")

    if prediction == 1:
        print("PASS")
    else:
        print("FAIL")

    if len(outputs) > 1:
        probs = outputs[1][0]
        print(f"Fail Probability : {probs[0]:.4f}")
        print(f"Pass Probability : {probs[1]:.4f}")

def main():
    session = load_model()

    print("Model Inputs:")
    for inp in session.get_inputs():
        print(
            f"Name={inp.name}, "
            f"Shape={inp.shape}, "
            f"Type={inp.type}"
        )

    print("\nModel Outputs:")
    for out in session.get_outputs():
        print(
            f"Name={out.name}, "
            f"Shape={out.shape}, "
            f"Type={out.type}"
        )

    predict_student(
        session,
        hours_studied=5,
        attendance_percent=85,
        previous_marks=70,
        assignment_score=80
    )

if __name__ == "__main__":
    main()