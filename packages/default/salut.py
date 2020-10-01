def main(args):
    message = "Salut, " + args.get("name", "mes amis") + "!";
    print(message)
    return {
        "body": {"message": message}
    }
