const attempts = {}

const bruteForceDetected = loginRequest => {
    const {sourceIP, successful} = loginRequest;
    attempts[sourceIP] = successful ? 0 : 1 + (0 | attempts[sourceIP]);
    return attempts >= 20;
}
