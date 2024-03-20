import vacuum_cleaner
import environment

def main():
    env = environment.Enviroment(5, 5)

    # Create a vacuum cleaner at position (0, 0) with 0 initial energy
    vacuum = vacuum_cleaner.VacuumCleaner(0, 0)

    # Start the vacuum cleaner
    vacuum.start_cleanup(env)

    env.print_status()

if __name__ == "__main__":
    main()